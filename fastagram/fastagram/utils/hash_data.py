from hashids import Hashids


def make_hash(instance):

    hashid = Hashids(
        salt=instance._meta.model_name,
        min_length=4,
    )

    return hashid.encode(instance.id)
