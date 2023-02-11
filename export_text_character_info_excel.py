from uasset_parser import parse_localization_files_to_excel
from uasset_parser import JA_TEXT_CHARACTER_INFO_ASSET_NAME, EN_TEXT_CHARACTER_INFO_ASSET_NAME, CN_TEXT_CHARACTER_INFO_ASSET_NAME, TW_TEXT_CHARACTER_INFO_ASSET_NAME

def main():
	parse_localization_files_to_excel(JA_TEXT_CHARACTER_INFO_ASSET_NAME, EN_TEXT_CHARACTER_INFO_ASSET_NAME, CN_TEXT_CHARACTER_INFO_ASSET_NAME, TW_TEXT_CHARACTER_INFO_ASSET_NAME)

if __name__ == '__main__':
    main()