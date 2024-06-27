from services.logger import setup_logger
from features.dynamoExtendedFileSupport.tools import get_summary, generate_flashcards, generate_concepts_from_img

logger = setup_logger(__name__)

def executor(file_url: str, app_type: str, verbose=True):
    if (verbose):
        logger.info(f"File URL loaded: {file_url}")
    flashcards = []

    if app_type == "4":
        flashcards = generate_concepts_from_img(file_url)
    else:
        summary = get_summary(file_url, app_type, verbose=verbose)
        flashcards = generate_flashcards(summary, verbose)
        

    sanitized_flashcards = []
    for flashcard in flashcards:
        if 'concept' in flashcard and 'definition' in flashcard:
            sanitized_flashcards.append({
                "concept": flashcard['concept'],
                "definition": flashcard['definition']
            })
        else:
            logger.warning(f"Malformed flashcard skipped: {flashcard}")

    return sanitized_flashcards 