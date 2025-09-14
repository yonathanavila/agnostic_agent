import json
from google.adk.agents import Agent

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


def get_price(treatment: str) -> dict:
    """Retrieves the current price for a specified treatment.

    Args:
        treatment (str): The name of the treatment for which to retrieve the price.

    Returns:
        dict: status and result or error msg.
    """

    if treatment.lower() in [
        "restauración",
        "restauracion dental",
        "restaurar",
        "restauración",
        "restauracion",
        "restauraciones dentales",
        "restauraciones",
        "restauracion de una muela",
        "restauracion de un diente",
        "restauración de una muela",
        "restauración de un diente",
    ]:

        t_identifier = "restauracion"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "limpieza",
        "limpieza dental",
        "limpiezas",
        "limpiezas dentales",
    ]:
        t_identifier = "limpieza"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "endodoncia",
        "endodoncia dental",
        "endodoncias",
        "endodoncias dentales",
    ]:
        t_identifier = "endodoncia"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "carillas",
        "carillas dentales",
        "carilla",
        "carilla dental",
    ]:
        t_identifier = "carillas"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "protesis",
        "protesis dentales",
    ]:
        t_identifier = "protesis"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "blanqueamiento",
        "blanqueamientos dentales",
    ]:
        t_identifier = "blanqueamiento"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "cirujia",
        "cirujias dentales",
    ]:
        t_identifier = "cirujia"
        t = treatment_price_database[t_identifier]

    elif treatment.lower() in [
        "evaluacion",
    ]:
        t_identifier = "evaluacion"
        t = treatment_price_database[t_identifier]

    else:
        return {
            "status": "error",
            "error_message": f"La información sobre el precio del tratamiento '{treatment}' no esta disponible. ",
        }

    return {"status": "success", "report": t}


def get_schedule_appointment(date: str) -> dict:
    """Returns the link to schedule appointment.

    Args:
        date (str): The date of the client was allowed to schedule an appointment.

    Returns:
        dict: status and result or error msg.
    """
    return {
        "status": "success",
        "report": (
            "Para poder agendar su cita, necesitaría su nombre completo. Muchas gracias"
            "✨ Perfecto. Aquí tiene el enlace para agendar su cita directamente: https://calendar.app.google/6VCo7i1WNHq6TZTn9 Solo debe seleccionar la fecha que más le convenga y completar sus datos. ¡Estaré esperándole para su cita!",
            "https://calendar.app.google/6VCo7i1WNHq6TZTn9",
        ),
    }


def get_allowed_treatment(treatment: str) -> dict:
    """Returns the treatment availables.

    Args:
        treatment (str): The name of the treatment available for schedule.

    Returns:
        dict: status and result or error msg.
    """

    if treatment.lower() in [
        "restauración",
        "restauracion dental",
        "restaurar",
        "restauración",
        "restauracion",
        "restauraciones dentales",
        "restauraciones",
        "restauracion de una muela",
        "restauracion de un diente",
        "restauración de una muela",
        "restauración de un diente",
    ]:

        t_identifier = "restauracion"

    elif treatment.lower() in [
        "limpieza",
        "limpieza dental",
        "limpiezas",
        "limpiezas dentales",
    ]:
        t_identifier = "limpieza"

    elif treatment.lower() in [
        "endodoncia",
        "endodoncia dental",
        "endodoncias",
        "endodoncias dentales",
    ]:
        t_identifier = "endodoncia"

    elif treatment.lower() in [
        "carillas",
        "carillas dentales",
        "carilla",
        "carilla dental",
    ]:
        t_identifier = "carillas"

    elif treatment.lower() in [
        "protesis",
        "protesis dentales",
    ]:
        t_identifier = "protesis"

    elif treatment.lower() in [
        "blanqueamiento",
        "blanqueamientos dentales",
    ]:
        t_identifier = "blanqueamiento"

    elif treatment.lower() in [
        "cirujia",
        "cirujias dentales",
    ]:
        t_identifier = "cirujia"

    else:
        return {
            "status": "error",
            "error_message": (f"Losentimos, no contamos con {treatment}."),
        }

    t = treatment_available[t_identifier]
    return {"status": "success", "report": t}


def get_identify_treatment(treatment: str) -> dict:
    """Identifies and provides a detailed description of a specific dental treatment. This tool should be used when the user asks for information about a treatment, such as what it consists of, what it's for, or its general details, but NOT when they ask for a price.

    Args:
        treatment (str): The name of the treatment that the patient ask.

    Returns:
        dict: status and result or error msg.
    """

    if treatment.lower() in [
        "restauración",
        "restauracion dental",
        "restaurar",
        "restauración",
        "restauracion",
        "restauraciones dentales",
        "restauraciones",
        "restauracion de una muela",
        "restauracion de un diente",
        "restauración de una muela",
        "restauración de un diente",
    ]:

        t_identifier = "restauracion"

    elif treatment.lower() in [
        "limpieza",
        "limpieza dental",
        "limpiezas",
        "limpiezas dentales",
    ]:
        t_identifier = "limpieza"

    elif treatment.lower() in [
        "endodoncia",
        "endodoncia dental",
        "endodoncias",
        "endodoncias dentales",
    ]:
        t_identifier = "endodoncia"

    elif treatment.lower() in [
        "carillas",
        "carillas dentales",
        "carilla",
        "carilla dental",
    ]:
        t_identifier = "carillas"

    elif treatment.lower() in [
        "protesis",
        "protesis dentales",
    ]:
        t_identifier = "protesis"

    elif treatment.lower() in [
        "blanqueamiento",
        "blanqueamientos",
        "blanqueamientos dentales",
    ]:
        t_identifier = "blanqueamiento"

    elif treatment.lower() in [
        "cirujia",
        "cirujias",
        "cirujias dentales",
    ]:
        t_identifier = "cirujia"

    else:
        return {
            "status": "error",
            "error_message": (f"Losentimos, no contamos con {treatment}."),
        }

    t = treatment_available[t_identifier]
    return {"status": "success", "report": t}


root_agent = Agent(
    name="dentist_agent",
    model="gemini-2.0-flash",
    description=(
        "Agente virtual de la Clínica Dental de la Dra. Alejandra Picado, clínica reconocida como experta en restauraciones dentales. La Dra. Picado cuenta con estudios y experiencia avanzada en tratamientos restaurativos, lo que le permite ofrecer soluciones de alta calidad en casos complejos como: dientes fracturados, caries extensas, dolor dental, restauraciones estéticas y dientes con compromiso estructural severo. La clínica se enfoca en conservar los dientes siempre que sea posible, evitando tratamientos innecesarios y utilizando protocolos y materiales de excelencia. El agente orienta, genera confianza, detecta intención de compra. El agente no brinda consulta ni diagnóstico por WhatsApp, pero sí orienta, genera confianza, detecta intención de compra y persuade al paciente para dar el primer paso: reservar su cita de evaluación clínica (L1500, incluye estudios y diagnóstico personalizado)."
    ),
    instruction="Eres un agente virtual profesional y empático de la Clínica Dental de la Dra. Alejandra Picado. Trata siempre al paciente de 'usted'.\n Aclarar que no se da consulta por WhatsApp, pero sí se puede orientar y explicar los tratamientos.\n Guiar siempre hacia el agendamiento de la cita de evaluación como punto de inicio.\n Guiar siempre hacia el agendamiento de la cita de evaluación como punto de inicio.\n Usar mensajes persuasivos que transmitan confianza y experiencia.\n Gestionar cancelaciones con empatía y proactividad, sugiriendo siempre reagendar.\n Detectar casos de urgencia (dolor, fracturas, inflamación) y priorizar la cita lo antes posible.\n Responder dudas con énfasis en el valor agregado: atención personalizada, protocolos rigurosos, materiales de primera calidad y tratamientos duraderos.",
    tools=[
        get_price,
        get_allowed_treatment,
        get_schedule_appointment,
        get_identify_treatment,
    ],
)
