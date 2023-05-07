from unittest.mock import Mock, patch
import tempfile
import os
import pytest
import pickle
from src.tracking.crawler import WebCrawler
from src.tracking.scraper import WebScraper
from src.tracking.transformer import Transformer
from src.tracking.db_handler import DBHandler
from src.tracking.flat_easy_finder import FlatEasyFinder


