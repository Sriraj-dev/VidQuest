import unicodedata
import pathway as pw

CHARS_PER_TOKEN = 3
PUNCTUATION = [".", "?", "!", "\n"]

@pw.udf
def chunk_texts(
    texts: str | list[str],
    min_tokens: int = 50,
    max_tokens: int = 500,
    encoding_name: str = "cl100k_base",
) -> list[str]:
    """
    Splits a given string or a list of strings into chunks based on token
    count.

    This function tokenizes the input texts and splits them into smaller parts ("chunks")
    ensuring that each chunk has a token count between `min_tokens` and
    `max_tokens`. It also attempts to break chunks at sensible points such as
    punctuation marks.

    Arguments:
        texts: string or list of strings.
        min_tokens: minimum tokens in a chunk of text.
        max_tokens: maximum size of a chunk in tokens.
        encoding_name: name of the encoding from `tiktoken`.

    Example:

    # >>> from pathway.stdlib.ml import chunk_texts
    # >>> import pathway as pw
    # >>> t  = pw.debug.table_from_markdown(
    # ...     '''| text
    # ... 1| cooltext'''
    # ... )
    # >>> t += t.select(chunks = chunk_texts(pw.this.text, min_tokens=1, max_tokens=1))
    # >>> pw.debug.compute_and_print(t, include_id=False)
    # text     | chunks
    # cooltext | ('cool', 'text')
    """
    import tiktoken

    if not isinstance(texts, str):
        texts = "\n".join(texts)

    tokenizer = tiktoken.get_encoding(encoding_name)
    text: str = texts
    text = normalize_unicode(text)
    tokens = tokenizer.encode_ordinary(text)
    output = []
    i = 0
    while i < len(tokens):
        chunk_tokens = tokens[i : i + max_tokens]
        chunk = tokenizer.decode(chunk_tokens)
        last_punctuation = max([chunk.rfind(p) for p in PUNCTUATION], default=-1)
        if last_punctuation != -1 and last_punctuation > CHARS_PER_TOKEN * min_tokens:
            chunk = chunk[: last_punctuation + 1]

        i += len(tokenizer.encode_ordinary(chunk))

        output.append(chunk)
    return output


def normalize_unicode(text: str):
    """
    Get rid of ligatures
    """
    return unicodedata.normalize("NFKC", text)
