import uasset_parser


def main():
	uasset_parser.repack_localization_files_from_excel(uasset_parser.TEXT_EXCEL_PATH, uasset_parser.CN_TEXT_ASSET_NAME)

if __name__ == '__main__':
    main()