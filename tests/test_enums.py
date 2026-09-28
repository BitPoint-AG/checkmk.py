from checkmk.enums import HostStates, ServiceStates


def test_host_states_cover_checkmk_notification_values() -> None:
    assert {s.name for s in HostStates} == {"UP", "DOWN", "UNREACHABLE"}
    assert HostStates.UNREACHABLE.value == 2


def test_service_states_cover_checkmk_notification_values() -> None:
    assert {s.name for s in ServiceStates} == {
        "OK",
        "WARNING",
        "CRITICAL",
        "UNKNOWN",
    }
    assert ServiceStates.UNKNOWN.value == 3
    assert ServiceStates.WARN is ServiceStates.WARNING
