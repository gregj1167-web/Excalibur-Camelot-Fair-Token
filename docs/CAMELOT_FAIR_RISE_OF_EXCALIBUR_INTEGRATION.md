# Camelot Fair: Rise of Excalibur Integration

This document provides the handoff contract for integrating Excalibur tokenomics and interactive dApp flows into the **Camelot-Fair-Rise-of-Excalibur** game repository.

## Integration Artifact

- Unity + UE5 shared config: [`../pkg/economy/excal_game_unity_ue5_integration.json`](../pkg/economy/excal_game_unity_ue5_integration.json)

## What the artifact includes

- EXCAL token configuration (with canonical EXS mapping)
- Enhanced tokenomics values required by gameplay loops
- Interactive dApp endpoints for wallet connection and forge flow
- Unity-specific asset + bridge mapping
- Unreal Engine 5 data asset + subsystem mapping

## Intended repository boundary

The game repository should consume this JSON as a source-of-truth configuration file and map it into:

- Unity ScriptableObject (`EXCALGameEconomyConfig`)
- Unreal Data Asset (`DA_EXCALTokenomics`)

No game-engine-specific source code is required in this repository for this handoff.
