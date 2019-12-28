import convertapi


def main():
    convertapi.api_secret = '0mKhFA6U5LcVkIMz'

    result = convertapi.convert('jpg', {'File': 'rasp/rasp.pdf'})

    for i, file in enumerate(result.files):
        file.save(f"images/{i}.jpeg")


if __name__ == '__main__':
    main()
