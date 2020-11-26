from datetime import datetime


class Logger:

    # The logger file
    log_file = "imagefilter.logger"

    def log(self, message):
        """
        :param message: The logger message
        :return:
        """
        # Get the current date
        now = datetime.now()
        # format the date
        timestamp = now.strftime("%Y/%m/%d %H:%M:%S")

        formated_message = f"{timestamp}  {message}"
        with open(self.log_file, "a") as f:
            f.write(formated_message + "\n")

    def dump_log(self):
        """
        Dump the logger file in the command line
        :return:
        """
        try:
            with open(self.log_file, "r") as f:
                print(f.read())
        except FileNotFoundError as e:
            print(f"Cannot open file {self.log_file}. error = {e}")
