from src.providers.transfermarket import get_player_id

def test_get_player_id():
    url = "https://www.transfermarkt.com/cristiano-ronaldo/profil/spieler/8198"
    assert get_player_id(url) == "8198"

def test_get_player_id_invalid():
    import pytest
    with pytest.raises(ValueError):
        get_player_id("https://www.transfermarkt.com/invalid-url")