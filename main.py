from app.config.settings import DATA_DIR, LOG_DIR
from app.data.downloader import Downloader
from app.data.yahoo_provider import YahooProvider


from app.data.provider_factory import create_provider
from app.data.downloader import Downloader



def main():
    print("Hello from quant-trading!")

    print("Data:", DATA_DIR)
    print("Logs:", LOG_DIR)

    
    provider = create_provider()
    downloader = Downloader(provider)

    df = downloader.download("MU")


    print(df.head())



if __name__ == "__main__":
    main()
