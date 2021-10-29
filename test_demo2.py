import demo2


def test_sample_analyze(gcs_content_uri):
    assert demo2.sample_analyze_entities(gcs_content_uri)
    pass
