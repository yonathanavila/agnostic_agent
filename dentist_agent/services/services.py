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
