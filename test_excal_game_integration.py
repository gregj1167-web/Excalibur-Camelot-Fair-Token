#!/usr/bin/env python3
"""
Validation tests for Camelot Fair game integration tokenomics config.
"""

import json
import os
from unittest import TestCase, main as unittest_main


class TestExcalGameIntegrationConfig(TestCase):
    """Validate the Unity/UE5 integration config shape."""

    def test_config_has_required_sections(self):
        repo_root = os.path.dirname(os.path.abspath(__file__))
        config_path = os.path.join(
            repo_root,
            "pkg",
            "economy",
            "excal_game_unity_ue5_integration.json",
        )

        with open(config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        self.assertEqual(
            config["integration"]["target_repository"],
            "Camelot-Fair-Rise-of-Excalibur",
        )
        self.assertEqual(config["token"]["symbol"], "EXCAL")
        self.assertEqual(config["token"]["canonical_symbol"], "EXS")
        self.assertEqual(config["token"]["max_supply"], 21_000_000)
        self.assertEqual(config["enhanced_tokenomics"]["forge_reward"], 50)
        self.assertEqual(config["interactive_dapp"]["forge_action"]["required_axiom_words"], 13)
        self.assertIn("wallet_connected", config["interactive_dapp"]["events"])
        self.assertEqual(config["unity"]["config_asset_name"], "EXCALGameEconomyConfig")
        self.assertEqual(config["ue5"]["data_asset_name"], "DA_EXCALTokenomics")


if __name__ == "__main__":
    unittest_main(verbosity=2)
