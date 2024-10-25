from app.config import (
    Config,
    ConfigApp,
    LogLevel,
    ConfigDatabase,
    ConfigTelemetry,
    ConfigStats,
    ConfigPseudonymApi,
)


def get_test_config() -> Config:
    return Config(
        app=ConfigApp(
            loglevel=LogLevel.error,
            provider_id="84de3f9c-0113-4fbb-af4b-215715e631bd",
            override_authentication_ura=None,
        ),
        database=ConfigDatabase(
            dsn="sqlite:///:memory:",
            create_tables=True,
        ),
        pseudonym_api=ConfigPseudonymApi(
            mock=True,
            endpoint="http://pseudonym",
            timeout=30,
            mtls_cert=None,
            mtls_key=None,
            mtls_ca=None,
        ),
        telemetry=ConfigTelemetry(
            enabled=False,
            endpoint=None,
            service_name=None,
            tracer_name=None,
        ),
        stats=ConfigStats(enabled=False, host=None, port=None, module_name=None),
    )
