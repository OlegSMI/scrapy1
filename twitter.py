import dataclasses
import datetime
import typing
from optparse import OptionParser

import snscrape.modules.twitter as sntwitter
from loguru import logger


parser = OptionParser()
parser.add_option("-T", "--tag", dest="tag",
                  help="tag for searching", metavar="Putin")
parser.add_option("-N", "--number", dest="number",
                  help="required number of tweets", metavar="100", default='100')
options, args = parser.parse_args()


@dataclasses.dataclass
class DescriptionURL:
	text: typing.Optional[str]
	url: str
	tcourl: str
	indices: typing.Tuple[int, int]


@dataclasses.dataclass
class User:
    username: str
    id: int
    displayname: typing.Optional[str] = None
    description: typing.Optional[str] = None 
    rawDescription: typing.Optional[str] = None
    descriptionUrls: typing.Optional[typing.List[DescriptionURL]] = None
    verified: typing.Optional[bool] = None
    created: typing.Optional[datetime.datetime] = None
    followersCount: typing.Optional[int] = None
    friendsCount: typing.Optional[int] = None
    statusesCount: typing.Optional[int] = None
    favouritesCount: typing.Optional[int] = None
    listedCount: typing.Optional[int] = None
    mediaCount: typing.Optional[int] = None
    location: typing.Optional[str] = None
    protected: typing.Optional[bool] = None
    linkUrl: typing.Optional[str] = None
    linkTcourl: typing.Optional[str] = None
    profileImageUrl: typing.Optional[str] = None
    profileBannerUrl: typing.Optional[str] = None

    def __str__(self):
        return self.username

    def __repr__(self):
        return self.username

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        if self.descriptionUrls:
            self.descriptionUrls = [DescriptionURL(**i) for i in self.descriptionUrls]


@dataclasses.dataclass
class Tweet:
    url: str
    date: datetime.datetime
    content: str
    renderedContent: str
    id: int
    user: 'User'
    replyCount: int
    retweetCount: int
    likeCount: int
    quoteCount: int
    conversationId: int
    lang: str
    source: str
    sourceUrl: typing.Optional[str] = None
    sourceLabel: typing.Optional[str] = None
    outlinks: typing.Optional[typing.List[str]] = None
    tcooutlinks: typing.Optional[typing.List[str]] = None
    media: typing.Optional[typing.List['Medium']] = None
    retweetedTweet: typing.Optional['Tweet'] = None
    quotedTweet: typing.Optional['Tweet'] = None
    inReplyToTweetId: typing.Optional[int] = None
    inReplyToUser: typing.Optional['User'] = None
    mentionedUsers: typing.Optional[typing.List['User']] = None
    coordinates: typing.Optional['Coordinates'] = None
    place: typing.Optional['Place'] = None
    hashtags: typing.Optional[typing.List[str]] = None
    cashtags: typing.Optional[typing.List[str]] = None

    def __init__(self, **kwargs):
        self.__dict__ = kwargs
        self.user = User(**self.user.__dict__)

    def __str__(self):
        return self.content

    def __repr__(self):
        return self.content


def parse_by_tag(tag: str, number: int):
    for i, tweet in enumerate(sntwitter.TwitterSearchScraper(tag).get_items()):
        logger.debug(i)
        if i >= int(number):
            return
        yield Tweet(**tweet.__dict__)


if __name__ == '__main__':
    tag = ' '.join([options.tag] + args).strip()
    r = list(parse_by_tag(tag, options.number))