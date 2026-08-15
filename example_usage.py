from client import MultiAgentCollaborativeDebugOrchestratorClient

def main():
    client = MultiAgentCollaborativeDebugOrchestratorClient()
    trace = "TypeError: Cannot read properties of undefined (reading 'user') at Auth.resolveUser"
    res = client.orchestrate_debug_session(trace, "src/auth.ts")
    print(f"Root Cause: {res['root_cause_analysis']}")
    print(f"Patch Verified: {res['patch_verified']}")
    print("Synthesized Diff Patch:")
    print(res["synthesized_diff_patch"])

if __name__ == "__main__":
    main()
