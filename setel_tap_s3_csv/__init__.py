"""
Tap S3 csv main script
"""

import tap_s3_csv
from setel_tap_s3_csv.sync import sync_stream

tap_s3_csv.sync_stream = sync_stream


class args:
    pass


import singer

LOGGER = tap_s3_csv.LOGGER
CONFIG_CONTRACT = tap_s3_csv.CONFIG_CONTRACT
list_files_in_bucket = tap_s3_csv.s3.list_files_in_bucket
setup_aws_client = tap_s3_csv.s3.setup_aws_client
do_discover = tap_s3_csv.do_discover
do_sync = tap_s3_csv.do_sync


@singer.utils.handle_top_exception(LOGGER)
def test_main() -> None:
    """
    Main function
    :return: None
    """
    # args = singer.utils.parse_args(REQUIRED_CONFIG_KEYS)
    args.config = singer.utils.load_json("/home/thai0125nt/.pipelinewise/target_vmo_s3_1/tap_thai_s3_1/config.json")
    args.properties = singer.utils.load_json(
        "/home/thai0125nt/.pipelinewise/target_vmo_s3_1/tap_thai_s3_1/properties.json")
    args.discover = None
    args.state = {}
    config = args.config

    # Reassign the config tables to the validated object
    config['tables'] = CONFIG_CONTRACT(config.get('tables', {}))

    try:
        for _ in list_files_in_bucket(config['bucket']):
            break
        LOGGER.warning("I have direct access to the bucket without assuming the configured role.")
    except Exception:
        setup_aws_client(config)

    if args.discover:
        do_discover(args.config)
    elif args.properties:
        do_sync(config, args.properties, args.state)


main = tap_s3_csv.main
if __name__ == '__main__':
    main()
