# hippocraticum-ai-consultation-sdk/client_public.py
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional, Union, BinaryIO
from .types import UNSET, Unset
from .client import AuthenticatedClient
from .api.crud.get_all_consultations_sessions_get import sync as _list_consults
from .api.crud.get_consultation_sessions_id_get import sync as _get_consult
from .api.crud.initialize_consultation_sessions_post import sync as _create_consult
from .api.crud.stop_consultation_sessions_id_stop_post import sync as _stop_consult
from .api.crud.delete_consultation_sessions_id_delete import sync as _delete_consult

from .api.results.get_transcript_sessions_id_transcript_get import sync as _get_transcript
from .api.results.get_speaker_segments_sessions_id_speaker_segments_get import sync as _get_speaker_segments
from .api.results.get_insights_sessions_id_insights_get import sync as _get_insights
from .api.results.get_symptoms_sessions_id_symptoms_get import sync as _get_symptoms
from .api.results.get_speaker_events_sessions_id_events_get import sync as _get_speaker_events
from .api.results.get_medical_questions_sessions_id_medical_questions_get import sync as _get_medical_questions
from .api.results.get_icd10_sessions_id_insights_icd10_get import sync as _get_icd10
from .api.results.get_follow_up_sessions_id_insights_follow_up_get import sync as _get_follow_up
from .api.results.get_differential_diagnosis_sessions_id_differential_dx_get import sync as _get_differential_diagnosis

from .api.reports.get_medical_report_sessions_id_report_type_of_medical_report_get import sync as _get_medical_report

from .api.operations.get_status_operation_operations_op_id_get import sync as _get_operation_status
from .api.operations.stream_status_operation_operations_op_id_events_get import sync as _stream_operation_events

from .api.post_process.post_processing_sessions_id_post_process_post import sync as _post_process_audio

from .tools import safe_call

from .models.pydantic_consultation_initialize_request import PydanticConsultationInitializeRequest
from .models.medical_response_format import MedicalResponseFormat
from .models.body_post_processing_sessions_id_post_process_post import BodyPostProcessingSessionsIdPostProcessPost
from .types import File

@dataclass
class _Config:
    base_url: str
    api_key: Optional[str] = None
    timeout: float = 30.0


class _Consultations:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call
    def list(self):
        """List all consultations
        
        Retrieve a list of all consultation sessions associated with the current API key.
        Returns basic information about each consultation.
        """
        return _list_consults(client=self._c)

    @safe_call
    def get(self, session_id: str):
        """Get specific consultation
        
        Retrieve detailed information about a specific consultation session.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _get_consult(client=self._c, id=session_id)

    @safe_call
    def create(self, body: PydanticConsultationInitializeRequest):
        """Create a new consultation session
        
        Initialize a new consultation session with specified type and features.
        Returns consultation ID and initial state.
        
        Args:
            body (PydanticConsultationInitializeRequest): Configuration for the new consultation
        """
        return _create_consult(client=self._c, body=body)

    @safe_call
    def stop(self, session_id: str):
        """Stop consultation session
        
        Stop an active consultation session. This will finalize the session and
        make results available for retrieval.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _stop_consult(client=self._c, id=session_id)

    @safe_call
    def delete(self, session_id: str):
        """Delete consultation
        
        Mark a consultation session as deleted. This is a soft delete operation.
        The consultation data may still be retrievable for a period of time.
        
        Args:
            session_id (str): Unique identifier for the consultation session to delete
        """
        return _delete_consult(client=self._c, id=session_id)


class _Results:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call
    def transcript(self, session_id: str):
        """Get consultation transcript"""
        return _get_transcript(client=self._c, id=session_id)

    @safe_call
    def speaker_segments(self, session_id: str):
        """Get speaker segments (diarisation)"""
        return _get_speaker_segments(client=self._c, id=session_id)

    @safe_call
    def insights(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get AI-generated insights"""
        return _get_insights(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def symptoms(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get extracted symptoms"""
        return _get_symptoms(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def events(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get consultation events"""
        return _get_speaker_events(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def medical_questions(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get medical questions"""
        return _get_medical_questions(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def icd10(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get ICD-10 codes"""
        return _get_icd10(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def follow_up(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get follow-up recommendations"""
        return _get_follow_up(client=self._c, id=session_id, use_language_translate=use_language_translate)

    @safe_call
    def differential_diagnosis(self, session_id: str, use_language_translate: Union[None, Unset, bool] = False):
        """Get differential diagnosis"""
        return _get_differential_diagnosis(client=self._c, id=session_id, use_language_translate=use_language_translate)


class _Reports:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call
    def medical_report(self, session_id: str, format: MedicalResponseFormat):
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
        return _get_medical_report(client=self._c, id=session_id, type_of_medical_report=format)
        
    @safe_call
    def dar(self, session_id: str):
        """Get DAR format medical report
        
        Retrieve a medical report in DAR (Data, Action, Response) format.
        This format focuses on clinical data, interventions taken, and patient responses.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.DAR)
        
    @safe_call
    def pie(self, session_id: str):
        """Get PIE format medical report
        
        Retrieve a medical report in PIE (Problem, Intervention, Evaluation) format.
        This format structures information around identified problems and their management.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.PIE)
        
    @safe_call
    def sbar(self, session_id: str):
        """Get SBAR format medical report
        
        Retrieve a medical report in SBAR (Situation, Background, Assessment, Recommendation) format.
        This format is commonly used for clinical communication and handoffs.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.SBAR)
        
    @safe_call
    def soap(self, session_id: str):
        """Get SOAP format medical report
        
        Retrieve a medical report in SOAP (Subjective, Objective, Assessment, Plan) format.
        This is the most common format for medical documentation.
        
        Args:
            session_id (str): Unique identifier for the consultation session
        """
        return _get_medical_report(client=self._c, id=session_id, type_of_medical_report=MedicalResponseFormat.SOAP)


class _Operations:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call
    def get_status(self, operation_id: str):
        """Get operation status
        
        Retrieve the current status and progress of a background operation (e.g., audio processing, AI analysis).
        Returns operation state, progress percentage, and any error information.
        
        Args:
            operation_id (str): Unique identifier for the operation
            
        Returns:
            Operation status including state, progress, and error information if any
        """
        return _get_operation_status(client=self._c, op_id=operation_id)
        
    @safe_call
    def stream_progress(self, operation_id: str):
        """Stream operation progress
        
        Stream real-time progress updates for a background operation using Server-Sent Events (SSE).
        Returns progress percentages and completion status until the operation finishes.
        
        This method is useful for tracking long-running operations like audio processing or AI analysis.
        
        Args:
            operation_id (str): Unique identifier for the operation to stream
            
        Returns:
            Real-time progress updates as Server-Sent Events
        """
        return _stream_operation_events(client=self._c, op_id=operation_id)
        
    # Convenience methods with alternative names
    @safe_call
    def status(self, operation_id: str):
        """Get operation status (alias for get_status)
        
        Args:
            operation_id (str): Unique identifier for the operation
        """
        return self.get_status(operation_id)
        
    @safe_call
    def stream(self, operation_id: str):
        """Stream operation events (alias for stream_progress)
        
        Args:
            operation_id (str): Unique identifier for the operation to stream
        """
        return self.stream_progress(operation_id)


class _PostProcess:
    def __init__(self, client: AuthenticatedClient):
        self._c = client

    @safe_call
    def upload_audio(self, session_id: str, audio_file: BinaryIO, filename: Optional[str] = None, mime_type: Optional[str] = None):
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
                result = client.post_process.upload_audio(
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
        return _post_process_audio(client=self._c, id=session_id, body=body)
        
    @safe_call
    def upload_audio_from_path(self, session_id: str, file_path: str, mime_type: Optional[str] = None):
        """Upload audio file from path for post-processing
        
        Convenience method to upload an audio file from a file path.
        
        Args:
            session_id (str): Unique identifier for the consultation session
            file_path (str): Path to the audio file
            mime_type (Optional[str]): MIME type of the audio file (auto-detected if not provided)
            
        Returns:
            Post-process response containing operation ID for tracking progress
            
        Example:
            result = client.post_process.upload_audio_from_path(
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
            return self.upload_audio(
                session_id=session_id,
                audio_file=f,
                filename=os.path.basename(file_path),
                mime_type=mime_type
            )
            
    # Convenience alias
    @safe_call
    def upload(self, session_id: str, audio_file: BinaryIO, filename: Optional[str] = None, mime_type: Optional[str] = None):
        """Upload audio (alias for upload_audio)
        
        Args:
            session_id (str): Unique identifier for the consultation session
            audio_file (BinaryIO): Audio file to upload
            filename (Optional[str]): Original filename (optional)
            mime_type (Optional[str]): MIME type of the audio file (optional)
        """
        return self.upload_audio(session_id, audio_file, filename, mime_type)


class ConsultationClient:
    """
    Публичный фасад, похожий на openai.OpenAI()
    """
    def __init__(self, base_url: str, api_key: Optional[str] = None, timeout: float = 30.0):
        self._c = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            timeout=timeout,
        )
        self.consultations = _Consultations(self._c)
        self.results = _Results(self._c)
        self.reports = _Reports(self._c)
        self.operations = _Operations(self._c)
        self.post_process = _PostProcess(self._c)

# Async-вариант (по аналогии), если генератор выдал async-функции:
# class AsyncConsultationClient: ...

