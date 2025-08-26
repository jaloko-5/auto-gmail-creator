from __future__ import annotations

import secrets
import string
from typing import Dict, Any, Set, Optional, List
from faker import Faker
import random


# Symbols curated to avoid CSV/terminal issues while staying "spicy"
SAFE_SYMBOLS = "!@#$%^&*()-_=+[]{}"


class AccountGenerator:
    """
    Generates fake user account data for simulation.

    Parameters
    ----------
    seed : Optional[int]
        If provided, seeds Faker and an internal RNG for reproducible names and
        username suffixes (passwords still use cryptographically secure randomness).
    recovery_domains : Optional[List[str]]
        Optional set of alternative providers to rotate for recovery emails.
    """

    def __init__(
        self,
        seed: Optional[int] = None,
        recovery_domains: Optional[List[str]] = None,
    ) -> None:
        self.fake = Faker()
        self.rand = random.Random(seed) if seed is not None else random.Random()
        if seed is not None:
            # Seed faker for reproducible names
            self.fake.seed_instance(seed)
        self._used_usernames: Set[str] = set()
        self.recovery_domains = recovery_domains or [
            "outlook.com",
            "yahoo.com",
            "proton.me",
            "zoho.com",
            "example.com",
        ]

    def generate_password(self, length: int = 12) -> str:
        """
        Generates a random password using secrets.

        Ensures at least one lower, upper, digit, and symbol from SAFE_SYMBOLS,
        then fills the rest randomly.
        """
        if length < 8:
            raise ValueError("Password length must be at least 8")

        pools = {
            "lower": string.ascii_lowercase,
            "upper": string.ascii_uppercase,
            "digit": string.digits,
            "sym": SAFE_SYMBOLS,
        }
        # Enforce minimum variety
        required = [
            secrets.choice(pools["lower"]),
            secrets.choice(pools["upper"]),
            secrets.choice(pools["digit"]),
            secrets.choice(pools["sym"]),
        ]
        all_chars = "".join(pools.values())
        remaining = [secrets.choice(all_chars) for _ in range(length - len(required))]
        pw_list = required + remaining
        self.rand.shuffle(pw_list)  # not security sensitive; only shuffles the list
        return "".join(pw_list)

    def _unique_username(self, first_name: str, last_name: str) -> str:
        """
        Builds a unique username within this generator's lifetime.
        """
        base = f"{first_name.lower()}.{last_name.lower()}"
        # Try up to a reasonable number of suffixes
        for _ in range(10_000):
            suffix = self.rand.randint(100, 999)
            candidate = f"{base}{suffix}"
            if candidate not in self._used_usernames:
                self._used_usernames.add(candidate)
                return candidate
        # Extremely unlikely fallback
        candidate = f"{base}{secrets.token_hex(2)}"
        self._used_usernames.add(candidate)
        return candidate

    def generate_account(self, password_length: int = 12) -> Dict[str, Any]:
        """Generates a single simulated Gmail account."""
        first_name = self.fake.first_name()
        last_name = self.fake.last_name()
        username = self._unique_username(first_name, last_name)
        email = f"{username}@gmail.com"
        recovery_domain = self.rand.choice(self.recovery_domains)
        recovery_email = f"{username}@{recovery_domain}"

        return {
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": self.generate_password(length=password_length),
            "recovery_email": recovery_email,
            "phone_verified": False,
        }

    # New neutral verb; retains the spirit of “demo only”
    def mark_phone_verified_demo(self, account: Dict[str, Any]) -> Dict[str, Any]:
        """
        Marks the account as phone-verified in the OUTPUT ONLY (DEMO).
        This does not interact with any real provider or perform any bypass.
        """
        print(f"[*] Marking phone verification as TRUE for {account['email']} [DEMO]")
        account["phone_verified"] = True
        return account

    # Backwards-compat alias (your tests keep working)
    def simulate_phone_verification_bypass(self, account: Dict[str, Any]) -> Dict[str, Any]:
        """
        [DEMO-ONLY] Back-compat alias to mark_phone_verified_demo. No real bypass.
        """
        return self.mark_phone_verified_demo(account)
