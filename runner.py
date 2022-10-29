import time

from sqlalchemy.orm import Session

from bridges import task_audio_bridge, submission_audio_bridge, submission_transcript_bridge, submission_task_bridge
from grader.grading_transcript import GradingTranscript, LegacyGrader
from model.model import engine
from utils.dictionary import Dictionary
from utils.task_determiner import TaskDeterminer

with Session(engine) as session:
    dictionary = Dictionary(session)
    grading_transcript_producer = GradingTranscript(dictionary)
    task_determiner = TaskDeterminer(session)
    grader = LegacyGrader(dictionary)
    task_audio_bridge.entry_point(session, grading_transcript_producer)
    submission_audio_bridge.entry_point(session)
    submission_transcript_bridge.entry_point(session, task_determiner)
    submission_task_bridge.entry_point(session, grader)
