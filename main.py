import vk_api
import datetime


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция. """
    # Код двухфакторной аутентификации,
    # который присылается по смс или уведомлением в мобильное приложение
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True
    return key, remember_device


def main():
    login, password = 'number', 'password'
    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler
    )
    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    res = vk.stats.get(group_id=194118559, fields='reach')
    print('subscribed', res[0]['activity']['subscribed'])
    print('comments', res[0]['activity']['comments'])
    print('likes', res[0]['activity']['likes'])
    print(res[0]['reach']['cities'])
    print(res[0]['reach']['age'])
    return [[res[0]['activity']['subscribed'], res[0]['activity']['comments'],
             res[0]['activity']['likes']], res[0]['reach']['age'], res[0]['reach']['cities']]


if __name__ == '__main__':
    main()
