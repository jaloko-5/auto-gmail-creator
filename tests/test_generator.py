from auto_gmail_creator.generator import AccountGenerator
import re


def test_generate_account():
    generator = AccountGenerator(seed=123)
    account = generator.generate_account()
    assert "first_name" in account
    assert "last_name" in account
    assert "email" in account and "@gmail.com" in account["email"]
    assert "password" in account and len(account["password"]) >= 12
    assert not account["phone_verified"]


def test_simulate_phone_verification_bypass():
    generator = AccountGenerator(seed=123)
    account = generator.generate_account()
    assert not account["phone_verified"]
    verified_account = generator.simulate_phone_verification_bypass(account)
    assert verified_account["phone_verified"]


def test_password_policy_default_length_and_charset():
    gen = AccountGenerator(seed=42)
    acc = gen.generate_account(password_length=16)
    pw = acc["password"]
    assert len(pw) == 16
    assert re.search(r"[a-z]", pw)
    assert re.search(r"[A-Z]", pw)
    assert re.search(r"[0-9]", pw)
    assert re.search(r"[!@#$%^&*()\\-_=+\\[\\]{}]", pw)


def test_uniqueness_of_usernames():
    gen = AccountGenerator(seed=999)
    emails = {gen.generate_account()["email"] for _ in range(100)}
    assert len(emails) == 100
