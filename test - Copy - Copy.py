import keepachangelog

changes = {
    "1.1.0": {
        "changed": [
            "Enhancement 1 (1.1.0)",
            "sub enhancement 1",
            "sub enhancement 2",
            "Enhancement 2 (1.1.0)",
        ],
        "release_date": "2018-05-31",
        "version": "1.1.0",
        "semantic_version": {
            "major": 1,
            "minor": 1,
            "patch": 0,
            "prerelease": None,
            "buildmetadata": None,
        },
        "url": "https://github.test_url/test_project/compare/v1.0.1...v1.1.0",
    },
    "1.0.1": {
        "fixed": [
            "Bug fix 1 (1.0.1)",
            "sub bug 1",
            "sub bug 2",
            "Bug fix 2 (1.0.1)",
        ],
        "release_date": "2018-05-31",
        "version": "1.0.1",
        "semantic_version": {
            "major": 1,
            "minor": 0,
            "patch": 1,
            "prerelease": None,
            "buildmetadata": None,
        },
        "url": "https://github.test_url/test_project/compare/v1.0.0...v1.0.1",
    },
    "1.0.0": {
        "deprecated": ["Known issue 1 (1.0.0)", "Known issue 2 (1.0.0)"],
        "release_date": "2017-04-10",
        "version": "1.0.0",
        "semantic_version": {
            "major": 1,
            "minor": 0,
            "patch": 0,
            "prerelease": None,
            "buildmetadata": None,
        },
        "url": "https://github.test_url/test_project/releases/tag/v1.0.0",
    },
}

changes = keepachangelog.to_dict("changelog.md")

#print