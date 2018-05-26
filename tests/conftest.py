import pytest
from moderator.utils import load_config
from moderator.consts import PROJ_ROOT
from moderator.main import init


@pytest.fixture
def loop(event_loop):
    return event_loop


@pytest.fixture
def conf():
    return load_config(PROJ_ROOT / 'config' / 'dev.yml')


@pytest.fixture
def api(loop, aiohttp_client, conf):
    app = loop.run_until_complete(init(loop, conf))
    return loop.run_until_complete(aiohttp_client(app))
