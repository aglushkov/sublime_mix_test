import os, re, sublime, sublime_plugin

class MixTestCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    window = self.view.window()
    wd = self.working_dir()
    window.run_command("exec", {
      "shell": True,
      "cmd": "mix test --color",
      "working_dir": self.working_dir()
    })

  def working_dir(self):
    file_name = self.view.file_name()
    match = re.search('(.+)/test/', file_name)
    if match:
      return match.group(1)
    else:
      return ''
