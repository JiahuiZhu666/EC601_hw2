import google.cloud
import language_v1


def sample_analyze_entities(gcs_content_uri):
    client = language_v1.LanguageServiceClient()

    type_ = language_v1.Document.Type.PLAIN_TEXT

    language = "en"
    document = {"gcs_content_uri": gcs_content_uri, "type_": type_, "language": language}

    # Available values: NONE, UTF8, UTF16, UTF32
    encoding_type = language_v1.EncodingType.UTF8

    response = client.analyze_entities(request={'document': document, 'encoding_type': encoding_type})
    # Loop through entitites returned from the API
    for entity in response.entities:
        print(u"Representative name for the entity: {}".format(entity.name))

        print(u"Entity type: {}".format(language_v1.Entity.Type(entity.type_).name))

        print(u"Salience score: {}".format(entity.salience))

        for metadata_name, metadata_value in entity.metadata.items():
            print(u"{}: {}".format(metadata_name, metadata_value))

        for mention in entity.mentions:
            print(u"Mention text: {}".format(mention.text.content))

            print(
                u"Mention type: {}".format(language_v1.EntityMention.Type(mention.type_).name)
            )

    print(u"Language of the text: {}".format(response.language))
