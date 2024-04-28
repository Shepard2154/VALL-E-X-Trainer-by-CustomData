from customs.make_custom_dataset import create_dataset


data_dir = "./customs/data_dir_russian"
create_dataset(data_dir, dataloader_process_only=True)