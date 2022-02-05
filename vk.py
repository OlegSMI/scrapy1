from optparse import OptionParser

import vk_api
from vk_api.streaming import VkStreaming
from loguru import logger


parser = OptionParser()
parser.add_option("-T", "--tag", dest="tag",
                  help="tag for searching", metavar="Putin", default='')
options, args = parser.parse_args()


SERVICE_KEY = '339847a1339847a1339847a13533eaab8d33398339847a16c9b4ef686c01b4a5fca91db'


def auth_handler():
    key = input("Enter authentication code: ")
    remember_device = True
    return key, remember_device


if __name__ == '__main__':
    tag = ' '.join([options.tag] + args).strip()

    vk_session = vk_api.VkApi(token=SERVICE_KEY)

    streaming = VkStreaming(vk_session)
    streaming.delete_all_rules()
    streaming.add_rule(tag, tag)
    for event in streaming.listen():
        logger.debug(event)




# Авторизация через пользователя (не поддерживает стриминг)
# login, password = 'login', 'password'
# vk_session = vk_api.VkApi(
#     login, password,
#     auth_handler=auth_handler
# )
# try:
#     vk_session.auth()
#     vk = vk_session.get_api()
# except vk_api.AuthError as error_msg:
#     print(error_msg)


# Запрос к newsfeed.search
# next_from = None
# while True:
#     r = vk_session.method('newsfeed.search', {
#         'q': 'путин',
#         'count': 200,
#         'start_from': next_from
#     })
#     items, next_from = r['items'], r['next_from']
#     logger.debug(items[0]['text'])