import uasset_parser


def main():
	uasset_parser.repack_localization_files_from_excel(uasset_parser.NARRATION_TABLE_EXCEL_PATH, uasset_parser.CN_NARRATION_TABLE_ASSET_NAME)

if __name__ == '__main__':
    main()