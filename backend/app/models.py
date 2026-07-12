from __future__ import annotations

from datetime import datetime, timezone

from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, JSON, String, Table, Text
from sqlalchemy.orm import relationship

from app.db.database import Base


def _utcnow() -> datetime:
    return datetime.now(timezone.utc)


disease_symptom = Table(
    "disease_symptom",
    Base.metadata,
    Column("disease_id", Integer, ForeignKey("diseases.id"), primary_key=True),
    Column("symptom_id", Integer, ForeignKey("symptoms.id"), primary_key=True),
)


class Disease(Base):
    __tablename__ = "diseases"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), unique=True, index=True, nullable=False)
    category = Column(String(80))
    description = Column(Text)
    severity_level = Column(String(30))
    icd_10_code = Column(String(20))
    created_at = Column(DateTime, default=_utcnow)

    symptoms = relationship("Symptom", secondary=disease_symptom, back_populates="diseases")
    medicines = relationship("Medicine", back_populates="disease", cascade="all, delete-orphan")


class Symptom(Base):
    __tablename__ = "symptoms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), unique=True, index=True, nullable=False)
    description = Column(Text)
    body_part = Column(String(80))
    created_at = Column(DateTime, default=_utcnow)

    diseases = relationship("Disease", secondary=disease_symptom, back_populates="symptoms")


class Medicine(Base):
    __tablename__ = "medicines"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120), nullable=False)
    generic_name = Column(String(120))
    category = Column(String(80))
    disease_id = Column(Integer, ForeignKey("diseases.id"), nullable=False)
    dosage = Column(String(120))
    frequency = Column(String(120))
    duration = Column(String(120))
    side_effects = Column(JSON, default=list)
    contraindications = Column(JSON, default=list)
    age_restrictions = Column(String(120))
    pregnancy_safe = Column(String(20))
    price_inr = Column(Float)
    prescription_required = Column(String(20))
    created_at = Column(DateTime, default=_utcnow)

    disease = relationship("Disease", back_populates="medicines")


class DiagnosticRecord(Base):
    __tablename__ = "diagnostic_records"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    selected_diseases = Column(JSON, default=list)
    symptoms = Column(JSON, default=list)
    severity = Column(String(30))
    image_path = Column(Text)
    cnn_predictions = Column(JSON, default=dict)
    rag_diagnosis = Column(Text)
    confidence_scores = Column(JSON, default=dict)
    suggested_medicines = Column(JSON, default=list)
    lifestyle_advice = Column(Text)
    followup_needed = Column(String(10))
    timestamp = Column(DateTime, default=_utcnow)


class EmergencyAlert(Base):
    __tablename__ = "emergency_alerts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    alert_type = Column(String(50))
    severity = Column(String(30))
    status = Column(String(30))
    latitude = Column(Float)
    longitude = Column(Float)
    hospitals_notified = Column(JSON, default=list)
    contacts_notified = Column(JSON, default=list)
    timestamp = Column(DateTime, default=_utcnow)
