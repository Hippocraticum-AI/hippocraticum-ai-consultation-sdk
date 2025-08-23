from hippocraticum_ai_consultation_sdk_link import ConsultationClient

client = ConsultationClient(base_url="http://", api_key="")

# Test that the client sets the X-API-KEY header correctly
print("Testing X-API-KEY header setup...")
http_client = client._c.get_httpx_client()
print(f"Headers: {dict(http_client.headers)}")

if "X-API-KEY" in http_client.headers:
    print(f"✅ X-API-KEY header is set to: {http_client.headers['X-API-KEY']}")
else:
    print("❌ X-API-KEY header is NOT set!")

# Test basic client functionality (will fail due to invalid URL, but should not crash on header setup)
try:
    print("\nTesting consultations.list()...")
    result = client.consultations.list()
    print(f"Success: {result}")
except Exception as e:
    print(f"Expected error (invalid server): {e}")
