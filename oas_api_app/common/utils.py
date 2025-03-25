def update_from_dto(model, dto):
    """
    Updates the given Item instance with data from CreateItemDTO
    Only updates fields that have non-null values in the DTO.

    Args:
        item (Item): The item to be updated.
        dto (CreateItemDTO): The data transfer object containing update information.

    Returns:
        Item: The updated item instance.
    """
    for field in vars(dto):
        value = getattr(dto, field)
        if value is not None:
            setattr(model, field, value)

def dto_to_dict(dto) -> dict:
    """
    Converts a DTO instance into a dictionary by iterating through its fields.

    Args:
        dto (CreateItemDTO): The data transfer object.

    Returns:
        dict: Dictionary representation of the DTO.
    """
    return {field: getattr(dto, field) for field in vars(dto)}
