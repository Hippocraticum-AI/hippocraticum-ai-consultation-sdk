# hippocraticum-ai-consultation-sdk/client_public_async.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union, BinaryIO
from .types import UNSET, Unset
from .client import AuthenticatedClient
from .api.crud.get_all_consultations_sessions_get import asyncio as _list_consults
from .api.crud.get_consultation_sessions_id_get import asyncio as _get_consult
from .api.crud.initialize_consultation_sessions_post import asyncio as _create_consult
from .api.crud.stop_consultation_sessions_id_stop_post import asyncio as _stop_consult
from .api.crud.delete_consultation_sessions_id_delete import asyncio as _delete_consult

from .api.results.get_transcript_sessions_id_transcript_get import asyncio as _get_transcript
from .api.results.get_speaker_segments_sessions_id_speaker_segments_get import asyncio as _get_speaker_segments
from .api.results.get_insights_sessions_id_insights_get import asyncio as _get_insights
from .api.results.get_symptoms_sessions_id_symptoms_get import asyncio as _get_symptoms
from .api.results.get_speaker_events_sessions_id_events_get import asyncio as _get_speaker_events
from .api.results.get_medical_questions_sessions_id_medical_questions_get import asyncio as _get_medical_questions
from .api.results.get_icd10_sessions_id_insights_icd10_get import asyncio as _get_icd10
from .api.results.get_follow_up_sessions_id_insights_follow_up_get import asyncio as _get_follow_up
from .api.results.get_differential_diagnosis_sessions_id_differential_dx_get import asyncio as _get_differential_diagnosis

from .api.reports.get_medical_report_sessions_id_report_type_of_medical_report_get import asyncio as _get_medical_report

from .api.operations.get_status_operation_operations_op_id_get import asyncio as _get_operation_status
from .api.operations.stream_status_operation_operations_op_id_events_get import asyncio as _stream_operation_events

from .api.post_process.post_processing_sessions_id_post_process_post import asyncio as _post_process_audio

from .api.default.health_check_health_get import asyncio_detailed as _health_check
from .api.default.root_get import asyncio_detailed as _root

from .tools import safe_call_async

from .models.pydantic_consultation_initialize_request import PydanticConsultationInitializeRequest
from .models.medical_response_format import MedicalResponseFormat
from .models.body_post_processing_sessions_id_post_process_post import BodyPostProcessingSessionsIdPostProcessPost
from .types import File

@dataclass
class _Config:
    base_url: str
    api_key: Optional[str] = None
    timeout: float = 30.0


class _AsyncConsultations:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def list(self):
        """List all consultations
        
        Retrieve a list of all consultation sessions associated with the current API key.
        Returns basic information about each consultation.
        """
        return await _list_consults(client=self._c)

    @safe_call_async
    async def get(self, session_id: str):
        """Get specific consultation
        
        Retrieve detailed information about a specific consultation session.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _get_consult(client=self._c, id=session_id)

    @safe_call_async
    async def create(self, body: PydanticConsultationInitializeRequest):
        """Create a new consultation session
        
        Initialize a new consultation session with specified type and features.
        Returns consultation ID and initial state.
        
        Args:
            body (PydanticConsultationInitializeRequest): Configuration for the new consultation
        """
        return await _create_consult(client=self._c, body=body)

    @safe_call_async
    async def stop(self, session_id: str):
        """Stop consultation session
        
        Stop an active consultation session. This will finalize the session and
        make results available for retrieval.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _stop_consult(client=self._c, id=session_id)

    @safe_call_async
    async def delete(self, session_id: str):
        """Delete consultation
        
        Mark a consultation session as deleted. This is a soft delete operation.
        The consultation data may still be retrievable for a period of time.
        
        Args:
            session_id (str): Unique identifier for the consultation session to delete
        """
        return await _delete_consult(client=self._c, id=session_id)


class _AsyncResults:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def transcript(self, session_id: str):
        """Get consultation transcript"""
        return await _get_transcript(client=self._c, id=session_id)

    @safe_call_async
    async def speaker_segments(self, session_id: str):
        """Get speaker segments (diarisation)"""
        return await _get_speaker_segments(client=self._c, id=session_id)

    @safe_call_async
    async def insights(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get AI-generated insights"""
        return await _get_insights(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def symptoms(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get extracted symptoms"""
        return await _get_symptoms(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def events(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get consultation events"""
        return await _get_speaker_events(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def medical_questions(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get medical questions"""
        return await _get_medical_questions(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def icd10(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get ICD-10 codes"""
        return await _get_icd10(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def follow_up(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get follow-up recommendations"""
        return await _get_follow_up(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call_async
    async def differential_diagnosis(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get differential diagnosis"""
        return await _get_differential_diagnosis(client=self._c, id=session_id, use_language_translate=use_language_translate)


class _AsyncReports:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def medical_report(self, session_id: str, format: MedicalResponseFormat):
        """Get medical report
        
        Retrieve a formatted medical report based on the consultation data.
        Available formats include DAR, PIE, SBAR, and SOAP for different medical use cases.
        
        Args:
            session_id (str): Unique identifier for the consultation session
            format (MedicalResponseFormat): Report format (DAR, PIE, SBAR, SOAP)
            
        Available formats:
            - DAR: Data, Action, Response format
            - PIE: Problem, Intervention, Evaluation format  
            - SBAR: Situation, Background, Assessment, Recommendation format
            - SOAP: Subjective, Objective, Assessment, Plan format
        """
        return await _get_medical_report(client=self._c, id=session_id, type_of_medical_report=format)
        
    @safe_call_async
    async def dar(self, session_id: str):
        """Get DAR format medical report
        
        Retrieve a medical report in DAR (Data, Action, Response) format.
        This format focuses on clinical data, interventions taken, and patient responses.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.DAR)
        
    @safe_call_async
    async def pie(self, session_id: str):
        """Get PIE format medical report
        
        Retrieve a medical report in PIE (Problem, Intervention, Evaluation) format.
        This format structures information around identified problems and their management.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.PIE)
        
    @safe_call_async
    async def sbar(self, session_id: str):
        """Get SBAR format medical report
        
        Retrieve a medical report in SBAR (Situation, Background, Assessment, Recommendation) format.
        This format is commonly used for clinical communication and handoffs.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.SBAR)
        
    @safe_call_async
    async def soap(self, session_id: str):
        """Get SOAP format medical report
        
        Retrieve a medical report in SOAP (Subjective, Objective, Assessment, Plan) format.
        This is the most common format for medical documentation.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return await _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.SOAP)


class _AsyncOperations:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def get_status(self, operation_id: str):
        """Get operation status
        
        Retrieve the current status and progress of a background operation (e.g., audio processing, AI analysis).
        Returns operation state, progress percentage, and any error information.
        
        Args:
            operation_id (str): Unique identifier for the operation
            
        Returns:
            Operation status including state, progress, and error information if any
        """
        return await _get_operation_status(client=self._c, op_id=operation_id)
        
    @safe_call_async
    async def stream_progress(self, operation_id: str):
        """Stream operation progress
        
        Stream real-time progress updates for a background operation using Server-Sent Events (SSE).
        Returns progress percentages and completion status until the operation finishes.
        
        This method is useful for tracking long-running operations like audio processing or AI analysis.
        
        Args:
            operation_id (str): Unique identifier for the operation to stream
            
        Returns:
            Real-time progress updates as Server-Sent Events
        """
        return await _stream_operation_events(client=self._c, op_id=operation_id)
        
    # Convenience methods with alternative names
    @safe_call_async
    async def status(self, operation_id: str):
        """Get operation status (alias for get_status)
        
        Args:
            operation_id (str): Unique identifier for the operation
        """
        return await self.get_status(operation_id)
        
    @safe_call_async
    async def stream(self, operation_id: str):
        """Stream operation events (alias for stream_progress)
        
        Args:
            operation_id (str): Unique identifier for the operation to stream
        """
        return await self.stream_progress(operation_id)


class _AsyncPostProcess:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def upload_audio(self, session_id: str, audio_file: BinaryIO, filename: Optional[str] = None, mime_type: Optional[str] = None):
        """Upload audio for post-processing
        
        Upload an audio file for a consultation session to trigger AI analysis including transcription,
        insights, symptoms analysis, differential diagnosis, and follow-up recommendations.
        Returns operation ID for tracking progress.
        
        Args:
            session_id (str): Unique identifier for the consultation session
            audio_file (BinaryIO): Audio file to upload (WAV format recommended)
            filename (Optional[str]): Original filename (optional)
            mime_type (Optional[str]): MIME type of the audio file (optional, defaults to audio/wav)
            
        Returns:
            Post-process response containing operation ID for tracking progress
            
        Example:
            with open('consultation_audio.wav', 'rb') as f:
                result = await client.post_process.upload_audio(
                    session_id='session-123',
                    audio_file=f,
                    filename='consultation_audio.wav',
                    mime_type='audio/wav'
                )
                operation_id = result.operation_id
        """
        # Create File object for upload
        audio_file_obj = File(
            payload=audio_file,
            file_name=filename or 'audio.wav',
            mime_type=mime_type or 'audio/wav'
        )
        
        # Create the request body
        body = BodyPostProcessingSessionsIdPostProcessPost(audio=audio_file_obj)
        
        # Make the API call
        return await _post_process_audio(client=self._c, id=session_id, body=body)
        
    @safe_call_async
    async def upload_audio_from_path(self, session_id: str, file_path: str, mime_type: Optional[str] = None):
        """Upload audio file from path for post-processing
        
        Convenience method to upload an audio file from a file path.
        
        Args:
            session_id (str): Unique identifier for the consultation session
            file_path (str): Path to the audio file
            mime_type (Optional[str]): MIME type of the audio file (auto-detected if not provided)
            
        Returns:
            Post-process response containing operation ID for tracking progress
            
        Example:
            result = await client.post_process.upload_audio_from_path(
                session_id='session-123',
                file_path='./consultation_audio.wav'
            )
        """
        import os
        
        # Auto-detect mime type if not provided
        if mime_type is None:
            extension = os.path.splitext(file_path)[1].lower()
            mime_types = {
                '.wav': 'audio/wav',
                '.mp3': 'audio/mpeg',
                '.m4a': 'audio/mp4',
                '.flac': 'audio/flac',
                '.ogg': 'audio/ogg'
            }
            mime_type = mime_types.get(extension, 'audio/wav')
        
        # Open file and upload
        with open(file_path, 'rb') as f:
            return await self.upload_audio(
                session_id=session_id,
                audio_file=f,
                filename=os.path.basename(file_path),
                mime_type=mime_type
            )
            
    # Convenience alias
    @safe_call_async
    async def upload(self, session_id: str, audio_file: BinaryIO, filename: Optional[str] = None, mime_type: Optional[str] = None):
        """Upload audio (alias for upload_audio)
        
        Args:
            session_id (str): Unique identifier for the consultation session
            audio_file (BinaryIO): Audio file to upload
            filename (Optional[str]): Original filename (optional)
            mime_type (Optional[str]): MIME type of the audio file (optional)
        """
        return await self.upload_audio(session_id, audio_file, filename, mime_type)


class _AsyncDefault:
    """Async default endpoints including health check and root endpoint"""
    
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call_async
    async def health_check(self):
        """Health Check
        
        Health check endpoint with database and MinIO status.
        Useful for monitoring service availability and dependencies.
        
        Returns:
            Health status response indicating service status
        """
        return await _health_check(client=self._c)
    
    @safe_call_async
    async def root(self):
        """Root endpoint
        
        Root endpoint returning basic API information.
        Can be used for basic connectivity testing.
        
        Returns:
            Root response with API information
        """
        return await _root(client=self._c)
        
    # Convenience aliases
    @safe_call_async
    async def health(self):
        """Health Check (alias for health_check)
        
        Returns:
            Health status response
        """
        return await self.health_check()
        
    @safe_call_async
    async def ping(self):
        """Ping service (alias for root)
        
        Returns:
            Root response for connectivity testing
        """
        return await self.root()


class AsyncConsultationClient:
    """
    Asynchronous public facade, similar to openai.AsyncOpenAI()
    """
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: float = 30.0):
        self._c = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=timeout,
        )
        self.consultations = _AsyncConsultations(self._c)
        self.results = _AsyncResults(self._c)
        self.reports = _AsyncReports(self._c)
        self.operations = _AsyncOperations(self._c)
        self.post_process = _AsyncPostProcess(self._c)
        self.default = _AsyncDefault(self._c)

