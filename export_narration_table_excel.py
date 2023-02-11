from uasset_parser import parse_localization_files_to_excel
from uasset_parser import JA_NARRATION_TABLE_ASSET_NAME, EN_NARRATION_TABLE_ASSET_NAME, CN_NARRATION_TABLE_ASSET_NAME, TW_NARRATION_TABLE_ASSET_NAME

def main():
	parse_localization_files_to_excel(JA_NARRATION_TABLE_ASSET_NAME, EN_NARRATION_TABLE_ASSET_NAME, CN_NARRATION_TABLE_ASSET_NAME, TW_NARRATION_TABLE_ASSET_NAME)

if __name__ == '__main__':
    main()