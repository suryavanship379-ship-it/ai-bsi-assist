def detect_intent(message):
    query = message.lower()

    if any(word in query for word in [
        "hello", "hi", "hey", "namaste"
    ]):
        return "greeting"

    if any(word in query for word in [
        "what is bis",
        "about bis",
        "tell me about bis",
        "bis means",
        "bureau of indian standards"
    ]):
        return "bis"

    if any(word in query for word in [
        "standard",
        "is number",
        "indian standard",
        "specification"
    ]):
        return "standard"

    if any(word in query for word in [
        "certification",
        "certificate",
        "license",
        "licence",
        "certify",
        "mandatory"
    ]):
        return "certification"

    if any(word in query for word in [
        "test",
        "testing",
        "tests"
    ]):
        return "testing"

    if any(word in query for word in [
        "lab",
        "laboratory",
        "where can i test"
    ]):
        return "laboratory"

    if any(word in query for word in [
        "document",
        "documents",
        "paperwork",
        "application"
    ]):
        return "documents"

    if any(word in query for word in [
        "process",
        "procedure",
        "steps",
        "how to",
        "journey",
        "next step"
    ]):
        return "journey"

    return "general"