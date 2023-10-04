# ent -> entity
# ex -> exception
def not_found_message(ent, ex) -> str:
    return f"No {ent} were found. Details: \n {ex}"

def not_found_by_id_message(ent, id, ex) -> str:
    return f"The {ent} with `id` {id} could not be found. Please ensure the `id` in your request is correct and try again. Details: \n {ex}"

def not_created_message(ent, ex) -> str:
    return f"The {ent} was not created. Please ensure the data in your request is correct and try again. Details: \n {ex}"
