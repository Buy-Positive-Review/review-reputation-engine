from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="review-reputation-engine",
    version="1.0.0",
    author="BuyPositiveReview.online",
    author_email="info@buypositivereview.online",
    description="A lightweight review reputation engine designed to organize, analyze, and monitor online review signals across business and review platforms.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://buypositivereview.online",
    project_urls={
        "Homepage": "https://buypositivereview.online",
        "GitHub": "https://github.com/Buy-Positive-Review/review-reputation-engine",
        "Documentation": "https://review-reputation-engine.readthedocs.io",
        "PyPI": "https://pypi.org/project/review-reputation-engine",
    },
    py_modules=["reputation_engine"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business",
    ],
    keywords=[
        "review-reputation-engine",
        "online-review-monitoring",
        "reputation-insights",
        "customer-feedback",
        "brand-presence",
        "review-visibility",
        "reputation-scoring",
        "review-management",
    ],
    entry_points={
        "console_scripts": [
            "reputation-engine=reputation_engine:main",
        ],
    },
)
