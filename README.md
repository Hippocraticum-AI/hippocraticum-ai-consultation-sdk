# 🏥 Hippocraticum AI Consultation SDK

**Python SDK for Hippocraticum AI Consultation API**

This library provides a convenient interface for working with the artificial intelligence platform API for medical consultations. The SDK supports both synchronous and asynchronous modes of operation.

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Main Classes](#main-classes)
- [API Reference](#api-reference)
- [Synchronous vs Asynchronous](#synchronous-vs-asynchronous)
- [Usage Examples](#usage-examples)
- [Extended Examples](./hippocraticum-ai-consultation-sdk/EXAMPLES.md)
- [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Support](#support)

## 🚀 Installation

```bash
pip install hippocraticum-ai-consultation-sdk
```

## ⚡ Quick Start

### Synchronous Client

```python
from hippocraticum_ai_consultation_sdk import ConsultationClient

# Create client
client = ConsultationClient(
    base_url="https://api.hippocraticum.com",
    api_key="your-api-key-here"
)

# Check API status
health = client.default.health_check()
print(f"API Status: {health.status_code}")

# Get list of consultations
consultations = client.consultations.list()
print(f"Consultations: {len(consultations)}")
```

### Asynchronous Client

```python
import asyncio
from hippocraticum_ai_consultation_sdk import AsyncConsultationClient

async def main():
    # Create asynchronous client
    client = AsyncConsultationClient(
        base_url="https://api.hippocraticum.com", 
        api_key="your-api-key-here"
    )
    
    # Check API status
    health = await client.default.health_check()
    print(f"API Status: {health.status_code}")
    
    # Get list of consultations
    consultations = await client.consultations.list()
    print(f"Consultations: {len(consultations)}")

asyncio.run(main())
```

## 🎯 Main Classes

The SDK provides two main classes for working with the API:

### `ConsultationClient` (Synchronous)
- Suitable for simple scripts and small applications
- Blocking API calls
- Ease of use

### `AsyncConsultationClient` (Asynchronous) 
- Suitable for web applications and high-load systems
- Non-blocking API calls with `async/await` support
- Ability to execute requests in parallel
- Better performance

> **Identical functionality** — both classes provide the same methods, the difference is only in synchronous/asynchronous execution.

## 📚 API Reference

Both clients contain the following modules:

### 🔧 `client.default` - Basic Operations
| Method | Description |
|-------|----------|
| `health_check()` / `health()` | Check API status and dependencies (DB, MinIO) |
| `root()` / `ping()` | Get API information, test connection |

### 📋 `client.consultations` - Consultation Management
| Method | Description |
|-------|----------|
| `list()` | Get list of all consultations |
| `get(session_id)` | Get information about specific consultation |
| `create(body)` | Create new consultation |
| `stop(session_id)` | Stop active consultation |
| `delete(session_id)` | Delete consultation |

### 📊 `client.results` - Results Retrieval
| Method | Description |
|-------|----------|
| `transcript(session_id)` | Get conversation transcript |
| `speaker_segments(session_id)` | Get speaker segments (diarization) |
| `insights(session_id)` | Get AI medical insights |
| `symptoms(session_id)` | Get extracted symptoms |
| `events(session_id)` | Get consultation events |
| `medical_questions(session_id)` | Get medical questions |
| `icd10(session_id)` | Get ICD-10 codes |
| `follow_up(session_id)` | Get follow-up recommendations |
| `differential_diagnosis(session_id)` | Get differential diagnosis |

### 📄 `client.reports` - Medical Reports
| Method | Description |
|-------|----------|
| `medical_report(session_id, format)` | Get report in specified format |
| `dar(session_id)` | DAR report (Data, Action, Response) |
| `pie(session_id)` | PIE report (Problem, Intervention, Evaluation) |
| `sbar(session_id)` | SBAR report (Situation, Background, Assessment, Recommendation) |
| `soap(session_id)` | SOAP report (Subjective, Objective, Assessment, Plan) |

### ⚙️ `client.operations` - Operations Tracking
| Method | Description |
|-------|----------|
| `get_status(operation_id)` / `status()` | Get background operation status |
| `stream_progress(operation_id)` / `stream()` | Stream operation progress (SSE) |

### 🎵 `client.post_process` - Audio Processing
| Method | Description |
|-------|----------|
| `upload_audio(session_id, audio_file)` | Upload audio file for processing |
| `upload_audio_from_path(session_id, file_path)` | Upload audio from file path |
| `upload(session_id, audio_file)` | Alias for upload_audio |


## 🎯 Usage Examples

### Service Health Check

```python
# Synchronous
def check_health():
    client = ConsultationClient(base_url="...", api_key="...")
    try:
        health = client.default.health_check()
        return health.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False

# Asynchronous
async def check_health_async():
    client = AsyncConsultationClient(base_url="...", api_key="...")
    try:
        health = await client.default.health_check()
        return health.status_code == 200
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
```

### Create and Process Consultation

```python
from hippocraticum_ai_consultation_sdk.models import PydanticConsultationInitializeRequest

# Synchronous
def process_consultation():
    client = ConsultationClient(base_url="...", api_key="...")
    
    # Create consultation
    request = PydanticConsultationInitializeRequest(
        consultation_type="audio",
        features=["transcription", "insights", "diagnosis"]
    )
    consultation = client.consultations.create(request)
    session_id = consultation.id
    
    # Upload audio
    with open("consultation_audio.wav", "rb") as f:
        result = client.post_process.upload_audio(session_id, f)
        operation_id = result.operation_id
    
    # Wait for processing completion
    while True:
        status = client.operations.get_status(operation_id)
        if status.completed:
            break
        time.sleep(1)
    
    # Get results
    transcript = client.results.transcript(session_id)
    insights = client.results.insights(session_id)
    diagnosis = client.results.differential_diagnosis(session_id)
    
    # Generate report
    soap_report = client.reports.soap(session_id)
    
    return {
        "transcript": transcript,
        "insights": insights, 
        "diagnosis": diagnosis,
        "report": soap_report
    }
```

### Parallel Processing (async only)

```python
import asyncio

async def process_multiple_consultations(session_ids):
    client = AsyncConsultationClient(base_url="...", api_key="...")
    
    # Process all consultations in parallel
    tasks = [
        client.results.transcript(session_id) 
        for session_id in session_ids
    ]
    
    transcripts = await asyncio.gather(*tasks)
    return transcripts

# Usage
session_ids = ["session-1", "session-2", "session-3"]
transcripts = await process_multiple_consultations(session_ids)
```

### Real-time Operation Monitoring

```python
# Stream operation progress
def monitor_operation(operation_id):
    client = ConsultationClient(base_url="...", api_key="...")
    
    # Get progress events
    for event in client.operations.stream_progress(operation_id):
        progress = event.get("progress", 0)
        print(f"Progress: {progress}%")
        
        if event.get("completed"):
            print("Operation completed!")
            break
```

## 🔧 Configuration

### Initialization Parameters

```python
client = ConsultationClient(
    base_url="https://api.hippocraticum.com",  # API URL
    api_key="your-api-key",                    # API key
    timeout=30.0                               # Request timeout (seconds)
)
```

### Error Handling

All methods use the `@safe_call` decorator for safe error handling:

```python
try:
    result = client.consultations.list()
except Exception as e:
    print(f"API call failed: {e}")
```

## 📖 API Documentation

Complete API documentation is available at: `https://api.hippocraticum.com/docs`

### Supported Audio Formats
- WAV (recommended)
- MP3
- M4A 
- FLAC
- OGG

### Medical Report Formats
- **DAR**: Data, Action, Response - focus on clinical data
- **PIE**: Problem, Intervention, Evaluation - structured by problems
- **SBAR**: Situation, Background, Assessment, Recommendation - for communication
- **SOAP**: Subjective, Objective, Assessment, Plan - most common format


## 📄 License

This project is licensed under the MIT License.

---

*Yaron Sigma - God bless him 2* 🙏
