from pydantic import BaseModel, ConfigDict


class _BaseSchema(BaseModel):
    model_config: ConfigDict = ConfigDict(
        populate_by_name=True, extra="ignore", use_enum_values=True
    )
