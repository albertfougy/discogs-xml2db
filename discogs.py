# coding: utf-8
from sqlalchemy import ARRAY, Column, Integer, MetaData, Numeric, Table, Text

metadata = MetaData()


t_artist = Table(
    'artist', metadata,
    Column('id', Integer, nullable=False),
    Column('name', Text, nullable=False),
    Column('realname', Text),
    Column('urls', ARRAY(Text())),
    Column('namevariations', ARRAY(Text())),
    Column('aliases', ARRAY(Text())),
    Column('releases', ARRAY(Integer())),
    Column('profile', Text),
    Column('members', ARRAY(Text())),
    Column('groups', ARRAY(Text())),
    Column('data_quality', Text)
)


t_artists_images = Table(
    'artists_images', metadata,
    Column('artist_id', Integer),
    Column('type', Text),
    Column('height', Integer),
    Column('width', Integer),
    Column('image_uri', Text)
)


t_country = Table(
    'country', metadata,
    Column('name', Text)
)


t_format = Table(
    'format', metadata,
    Column('name', Text, nullable=False)
)


t_genre = Table(
    'genre', metadata,
    Column('id', Integer, nullable=False),
    Column('name', Text),
    Column('parent_genre', Integer),
    Column('sub_genre', Integer)
)


t_label = Table(
    'label', metadata,
    Column('id', Integer, nullable=False),
    Column('name', Text, nullable=False),
    Column('contactinfo', Text),
    Column('profile', Text),
    Column('parent_label', Text),
    Column('sublabels', ARRAY(Text())),
    Column('urls', ARRAY(Text())),
    Column('data_quality', Text)
)


t_labels_images = Table(
    'labels_images', metadata,
    Column('label_id', Integer),
    Column('type', Text),
    Column('height', Integer),
    Column('width', Integer),
    Column('image_uri', Text)
)


t_master = Table(
    'master', metadata,
    Column('id', Integer, nullable=False),
    Column('title', Text),
    Column('main_release', Integer, nullable=False),
    Column('year', Integer),
    Column('notes', Text),
    Column('genres', Text),
    Column('styles', Text),
    Column('role', Text),
    Column('data_quality', Text)
)


t_masters_artists = Table(
    'masters_artists', metadata,
    Column('artist_name', Text),
    Column('master_id', Integer)
)


t_masters_artists_joins = Table(
    'masters_artists_joins', metadata,
    Column('artist1', Text),
    Column('artist2', Text),
    Column('join_relation', Text),
    Column('master_id', Integer)
)


t_masters_extraartists = Table(
    'masters_extraartists', metadata,
    Column('master_id', Integer),
    Column('artist_name', Text),
    Column('roles', ARRAY(Text()))
)


t_masters_formats = Table(
    'masters_formats', metadata,
    Column('master_id', Integer),
    Column('format_name', Text),
    Column('qty', Integer),
    Column('descriptions', ARRAY(Text()))
)


t_masters_images = Table(
    'masters_images', metadata,
    Column('master_id', Integer),
    Column('type', Text),
    Column('height', Integer),
    Column('width', Integer),
    Column('image_uri', Text)
)


t_release = Table(
    'release', metadata,
    Column('id', Integer, nullable=False),
    Column('status', Text),
    Column('title', Text),
    Column('country', Text),
    Column('released', Text),
    Column('barcode', Text),
    Column('notes', Text),
    Column('genres', Text),
    Column('styles', Text),
    Column('master_id', Integer),
    Column('data_quality', Text)
)


t_releases_artists = Table(
    'releases_artists', metadata,
    Column('release_id', Integer),
    Column('position', Integer),
    Column('artist_id', Integer),
    Column('artist_name', Text),
    Column('anv', Text),
    Column('join_relation', Text)
)


t_releases_extraartists = Table(
    'releases_extraartists', metadata,
    Column('release_id', Integer),
    Column('artist_id', Integer),
    Column('artist_name', Text),
    Column('anv', Text),
    Column('role', Text)
)


t_releases_formats = Table(
    'releases_formats', metadata,
    Column('release_id', Integer),
    Column('position', Integer),
    Column('format_name', Text),
    Column('qty', Numeric(100, 0)),
    Column('descriptions', ARRAY(Text()))
)


t_releases_images = Table(
    'releases_images', metadata,
    Column('release_id', Integer),
    Column('type', Text),
    Column('height', Integer),
    Column('width', Integer),
    Column('image_uri', Text)
)


t_releases_labels = Table(
    'releases_labels', metadata,
    Column('label', Text),
    Column('release_id', Integer),
    Column('catno', Text)
)


t_role = Table(
    'role', metadata,
    Column('role_name', Text)
)


t_track = Table(
    'track', metadata,
    Column('release_id', Integer),
    Column('position', Text),
    Column('track_id', Text),
    Column('title', Text),
    Column('duration', Text),
    Column('trackno', Integer)
)


t_tracks_artists = Table(
    'tracks_artists', metadata,
    Column('track_id', Text),
    Column('position', Integer),
    Column('artist_id', Integer),
    Column('artist_name', Text),
    Column('anv', Text),
    Column('join_relation', Text)
)


t_tracks_extraartists = Table(
    'tracks_extraartists', metadata,
    Column('track_id', Text),
    Column('artist_id', Integer),
    Column('artist_name', Text),
    Column('anv', Text),
    Column('role', Text),
    Column('data_quality', Text)
)
