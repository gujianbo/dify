from enum import Enum


class Field(Enum):
    CONTENT_KEY = "page_content"
    CONTENT_KEY_TOKEN = "page_content_token"
    METADATA_KEY = "metadata"
    GROUP_KEY = "group_id"
    VECTOR = "vector"
    # Sparse Vector aims to support full text search
    SPARSE_VECTOR = "sparse_vector"
    TEXT_KEY = "text"
    PRIMARY_KEY = "id"
    DOC_ID = "metadata.doc_id"
    DOCUMENT_ID = "metadata.document_id"
