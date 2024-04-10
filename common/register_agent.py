from qwen_agent.utils.utils import logger

AGENT_REGISTRY = {}


def register_agent(name, allow_overwrite=False):

    def decorator(cls):
        if name in AGENT_REGISTRY:
            if allow_overwrite:
                logger.warning(
                    f'Tool `{name}` already exists! Overwriting with class {cls}.'
                )
            else:
                raise ValueError(
                    f'Tool `{name}` already exists! Please ensure that the tool name is unique.'
                )
        if cls.name and (cls.name != name):
            raise ValueError(
                f'{cls.__name__}.name="{cls.name}" conflicts with @register_agent(name="{name}").'
            )
        cls.name = name
        AGENT_REGISTRY[name] = cls

        return cls

    return decorator
