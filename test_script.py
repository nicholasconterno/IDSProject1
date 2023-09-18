import unittest
import os
import subprocess

TEST_MD_PATH = "test_generated_markdown.md"
TEST_HIST_PATH = "test_histogram.png"

class TestScriptExecution(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        subprocess.run(["python", "main.py",TEST_MD_PATH,TEST_HIST_PATH])
    
    def test_script_runs_without_errors(self):
        # This will raise an error if the script has an error
        result = subprocess.run(["python", "main.py",TEST_MD_PATH, TEST_HIST_PATH], \
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0)

    def test_markdown_file_generation(self):
        # Assuming running the script generates the markdown file
        self.assertTrue(os.path.exists(TEST_MD_PATH))

    def test_markdown_file_content(self):
        with open(TEST_MD_PATH, 'r') as file:
            content = file.read()
            self.assertTrue(len(content) > 0)

    def test_histogram_image_generation(self):
        # Assuming the script generates an image named histogram.png
        self.assertTrue(os.path.exists(TEST_HIST_PATH))
    @classmethod
    def tearDownClass(cls):
        if os.path.exists(TEST_MD_PATH):
            os.remove(TEST_MD_PATH)
        if os.path.exists(TEST_HIST_PATH):
            os.remove(TEST_HIST_PATH)


if __name__ == '__main__':
    unittest.main()
