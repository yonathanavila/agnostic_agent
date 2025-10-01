# File: dentist_agent/data/data.py

import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional

# Treatment data
treatment_available = {
    "limpieza": {"Limpieza de rutina", "Limpieza profunda/restaurativa"},
    "endodoncia": {
        "Molares",
        "Premolare e incisivos",
    },
    "restauracion": {
        "Resinas convencionales",
        "Restauraciones cerámicas (Emax, zirconio)",
        "Refuerzo interno con fibras de vidrio (Ribbon)",
    },
    "carillas": {
        "Carillas de resina estratificada (directa o indirecta)",
        "Carillas cerámicas (Emax/Zirconio)",
    },
    "protesis": {
        "Prótesis fija (puente cerámico)",
        "Prótesis removible de cromo cobalto",
        "Prótesis total (sin transitoria)",
        "Prótesis total con prótesis transitoria de cicatrización",
    },
    "blanqueamiento": {
        "Blanqueamiento básico",
        "Blanqueamiento avanzado",
    },
    "cirujia": {
        "Exodoncia simple o quirúrgica",
        "Cirugías mayores (como frenillos, cortes de hueso, implantes)",
    },
}

treatment_price_database = {
    "limpieza": "Limpieza de rutina: L1,500. Limpieza profunda/restaurativa: L2,500 (según necesidad del paciente y conservación de restauraciones previas).",
    "endodoncia": "Molares desde L.6,800. Premolares e incisivos: varía según la complejidad (el retratamiento suele ser más costoso).",
    "restauracion": "Resinas convencionales: desde L2,500. Restauraciones cerámicas (Emax, zirconio): hasta L9,500 por diente. Refuerzo interno con fibras de vidrio (Ribbon): según evaluación (no existe un precio estándar, cada caso se evalúa individualmente).",
    "carillas": "Carillas de resina estratificada: L6,000 por diente. Carillas cerámicas (Emax/Zirconio): L10,500 por diente (tratamientos altamente estéticos, duraderos y con resultados naturales).",
    "protesis": "Prótesis fija (puente cerámico): L9,500 por unidad dental. Prótesis removible de cromo cobalto: L15,000. Prótesis total (sin transitoria): L8,500 cada una. Prótesis total con prótesis transitoria de cicatrización: L12,500 cada una.",
    "blanqueamiento": "Blanqueamiento básico: L6,500. Blanqueamiento avanzado: L9,500.",
    "cirujia": "Exodoncia simple o quirúrgica: según complejidad. Cirugías mayores (como frenillos, cortes de hueso, implantes): requieren estudios previos. Precios van desde L1,800 a L6,000.",
    "evaluacion": "La evaluación tiene un precio de L1,500",
}
