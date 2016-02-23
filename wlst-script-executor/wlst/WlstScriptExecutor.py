from abc import ABCMeta, abstractmethod
from subprocess import run
import os
import platform

class WlstScriptExecutor(metaclass=ABCMeta):
	def __init__(self, **kwargs):
		self.oracle_home = kwargs['oracle_home']

		self.wlst_command = self._build_wlst_command()


	@abstractmethod
	def _build_wlst_command(self):
		pass

	def execute_wslt_script(self, wlst_script, *args):
		command = []
		command.append(self.wlst_command)
		command.append(wlst_script)

		for arg in args:
			command.append(arg)

		result = run(command, shell=False)
		return result.returncode


class Soa1213WlstScriptExecutor(WlstScriptExecutor):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)


	def _build_wlst_command(self):
		# Requires the servicebus.jar to be set in the classpath.
		# Usually it is added through modification of setWlstEnv.sh
		export_command = os.path.join(self.oracle_home, 'soa', 'common', 'bin', 'wlst')
		
		op_sys = platform.system()
		if op_sys == 'Windows':
			bat_ext = '.bat'
			cmd_ext = '.cmd'
			if os.path.exists(export_command + bat_ext) and os.path.isfile(export_command + bat_ext):
				return export_command + bat_ext
			elif os.path.exists(export_command + cmd_ext) and os.path.isfile(export_command + cmd_ext):
				return export_command + cmd_ext
			else:
				pass
		elif op_sys == 'Linux' or op_sys == 'Darwin':
			return export_command + '.sh'
		else:
			# TODO: raise exception
			pass
