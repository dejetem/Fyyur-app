"""
Artist, Venue and Show models
"""
# Imports

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Models.

class Venue(db.Model):
    __tablename__ = 'venue'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String(120),nullable=False)
    website_link = db.Column(db.String(500))
    seeking_talent = db.Column(db.Boolean,default=False)
    seeking_description = db.Column(db.Text)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    past_shows_count = db.Column(db.Integer, default=0)
    shows = db.relationship('Show',backref='venue',lazy=True,
                        cascade="save-update, merge, delete")

class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website_link = db.Column(db.String(500))
    seeking_venue = db.Column(db.Boolean,default=False)
    seeking_description = db.Column(db.Text)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    past_shows_count = db.Column(db.Integer, default=0)
    shows = db.relationship('Show',backref='artist',lazy=True,
                        cascade="save-update, merge, delete")


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer,db.ForeignKey('artist.id')
                          ,nullable=False)
    venue_id = db.Column(db.Integer,db.ForeignKey('venue.id')
                          ,nullable=False)
    upcoming = db.Column(db.Boolean, nullable=False, default=True)


'''
class Venue(db.Model):
    __tablename__ = 'venues'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    genres = db.Column(db.String(120),nullable=False)
    website = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean,default=False)
    seeking_description = db.Column(db.Text)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    past_shows_count = db.Column(db.Integer, default=0)
    artists = db.relationship('Artist', secondary='shows', lazy=True,
                        cascade="save-update, merge, delete")
    shows = db.relationship('Show', backref=('venues'), lazy=True,
                        cascade="save-update, merge, delete")
    def to_dict(self):
        """ Returns a dictinary of vevenuesnues """
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address,
            'phone': self.phone,
            'genres': self.genres.split(','),  
            'image_link': self.image_link,
            'facebook_link': self.facebook_link,
            'website': self.website,
            'seeking_talent': self.seeking_talent,
            'seeking_description': self.seeking_description,
            'upcoming_shows_count': self.upcoming_shows_count,
            'past_shows_count': self.past_shows_count,
        }

    def __repr__(self):
        return f'<Venue {self.id} {self.name}>'

class Artist(db.Model):
    __tablename__ = 'artists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    city = db.Column(db.String(120), nullable=False)
    state = db.Column(db.String(120), nullable=False)
    phone = db.Column(db.String(120), nullable=False)
    genres = db.Column(db.String(120), nullable=False)
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))

    # TODO: implement any missing fields, as a database migration using Flask-Migrate
    website = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean,default=False)
    seeking_description = db.Column(db.Text)
    upcoming_shows_count = db.Column(db.Integer, default=0)
    past_shows_count = db.Column(db.Integer, default=0)
    venues = db.relationship('Venue', secondary='shows' ,lazy=True,
                        cascade="save-update, merge, delete")
    shows = db.relationship('Show', backref=('artists'),lazy=True,
                        cascade="save-update, merge, delete")
    def to_dict(self):
        """ Returns a dictinary of artists """
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'genres': self.genres.split(','),  # convert string to list
            'image_link': self.image_link,
            'facebook_link': self.facebook_link,
            'website': self.website,
            'seeking_venue': self.seeking_venue,
            'seeking_description': self.seeking_description,
            'upcoming_shows_count': self.upcoming_shows_count,
            'past_shows_count': self.past_shows_count,
        }
        
    def __repr__(self):
        return f'<Artist {self.id} {self.name}>'


# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.
class Show(db.Model):
    __tablename__ = 'shows'
    id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime, nullable=False)
    artist_id = db.Column(db.Integer,db.ForeignKey('artists.id')
                          ,nullable=False)
    venue_id = db.Column(db.Integer,db.ForeignKey('venues.id')
                          ,nullable=False)
    upcoming = db.Column(db.Boolean, nullable=False, default=True)
    venue = db.relationship('Venue')
    artist = db.relationship('Artist')

    def show_artist(self):
        """Returns a dictinary of artists for the show"""
        return {
            'artist_id': self.artist_id,
            'artist_name': self.artists.name,
            'artist_image_link': self.artists.image_link,
            # convert datetime to string
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        }

    def show_venue(self):
        """ Returns a dictinary of venues for the show """
        return {
            'venue_id': self.venue_id,
            'venue_name': self.venues.name,
            'venue_image_link': self.venues.image_link,
            # convert datetime to string
            'start_time': self.start_time.strftime('%Y-%m-%d %H:%M:%S')
        }
'''
            