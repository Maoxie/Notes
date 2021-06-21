#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""
@author: yangzhitao
@license: Copyright 2017-2020, LineZoneData.
@contact: yangzhitao@linezonedata.com
@software: pycharm
@time: 2019/12/12 18:53
@desc: 
"""

from enum import Enum
import os


class NotSupportOperation(Exception):
    msg = "不支持的操作"


class ProjectStatesEnum(Enum):
    """项目状态枚举类"""
    SAVED = 'saved'
    SUBMITTED = 'submitted'
    APPROVED = 'approved'
    FINISHING_APPLYING = 'finishing_applying'
    FINISHED = 'finished'
    TRANSFER_APPLYING = 'transfer_applying'

    # TERMINATION_APPLYING = 'termination_applying'
    # TERMINATED = 'terminated'


class ProjectContext:
    """
    Context类
    """
    def __init__(self, state_value):
        self.state = self._get_concrete_state(state_value)

    @classmethod
    def _get_concrete_state(cls, state_value):
        """获取具体的状态类"""
        states_map = {
            ProjectStatesEnum.SAVED.value: ProjectSavedState(),
            ProjectStatesEnum.SUBMITTED.value: ProjectSubmittedState(),
            ProjectStatesEnum.APPROVED.value: ProjectApprovedState(),
            ProjectStatesEnum.FINISHING_APPLYING.value: ProjectFinishingApplyingState(),
            ProjectStatesEnum.FINISHED.value: ProjectFinishedState(),
            ProjectStatesEnum.TRANSFER_APPLYING.value: ProjectTransferApplyingState(),

            # ProjectStatesEnum.TERMINATION_APPLYING.value: ProjectTerminationApplyingState(),
            # ProjectStatesEnum.TERMINATED.value: ProjectTerminatedState(),
        }
        return states_map[state_value]

    def _change_state(self, new_state):
        self.state = self._get_concrete_state(new_state)

    def handle(self, operation, *arg, **kwargs):
        return self.state.handle(self, operation, *arg, **kwargs)


class ProjectState:
    """抽象的项目状态类"""
    @property
    def value(self):
        raise NotImplementedError

    def _get_handler(self, operation):
        handler = getattr(self, operation, None)
        if not handler or not callable(handler):
            raise NotSupportOperation("当前状态是：{}，不能进行{}操作".format(self.value, operation))
        return handler
    
    def handle(self, context, operation, *arg, **kwargs):
        handler = self._get_handler(operation)
        return handler(context, *arg, **kwargs)


class ProjectSavedState(ProjectState):
    """状态：已保存"""
    @property
    def value(self):
        return ProjectStatesEnum.SAVED.value

    @staticmethod
    def update(context, **kwargs):
        print(">> 操作：编辑")

    @staticmethod
    def delete(context, **kwargs):
        print(">> 操作：删除")

    @staticmethod
    def submit(context, **kwargs):
        print(">> 操作：提交申请")
        context._change_state(ProjectStatesEnum.SUBMITTED.value)


class ProjectSubmittedState(ProjectState):
    """状态：已审批"""
    @property
    def value(self):
        return ProjectStatesEnum.SUBMITTED.value

    @staticmethod
    def drawback(context, **kwarg):
        print(">> 操作：撤回")
        context._change_state(ProjectStatesEnum.SAVED.value)

    @staticmethod
    def refuse(context, **kwarg):
        print(">> 操作：驳回")
        context._change_state(ProjectStatesEnum.SAVED.value)

    @staticmethod
    def approve(context, **kwarg):
        print(">> 操作：通过提交申请")
        context._change_state(ProjectStatesEnum.APPROVED.value)


class ProjectApprovedState(ProjectState):
    """状态：已审批"""
    @property
    def value(self):
        return ProjectStatesEnum.APPROVED.value

    @staticmethod
    def apply_for_finishing(context, **kwarg):
        print(">> 操作：申请结束")
        context._change_state(ProjectStatesEnum.FINISHED.value)

    @staticmethod
    def apply_for_transfer(context, **kwarg):
        print(">> 操作：申请移交")
        context._change_state(ProjectStatesEnum.TRANSFER_APPLYING.value)

    # @staticmethod
    # def apply_for_terminate(context, **kwarg):
    #     print("申请终止")
    #     context._change_state(ProjectStatesEnum.TERMINATION_APPLYING.value)


class ProjectTransferApplyingState(ProjectState):
    """状态：移交申请中"""
    @property
    def value(self):
        return ProjectStatesEnum.TRANSFER_APPLYING.value

    @staticmethod
    def drawback(context, **kwarg):
        print(">> 操作：撤回")
        context._change_state(ProjectStatesEnum.APPROVED.value)

    @staticmethod
    def refuse(context, **kwarg):
        print(">> 操作：驳回")
        context._change_state(ProjectStatesEnum.APPROVED.value)

    @staticmethod
    def approve(context, **kwarg):
        print(">> 操作：通过移交申请")
        context._change_state(ProjectStatesEnum.APPROVED.value)


class ProjectFinishingApplyingState(ProjectState):
    """状态：结束申请中"""
    @property
    def value(self):
        return ProjectStatesEnum.FINISHING_APPLYING.value

    @staticmethod
    def drawback(context, **kwarg):
        print(">> 操作：撤回")
        context._change_state(ProjectStatesEnum.APPROVED.value)

    @staticmethod
    def refuse(context, **kwarg):
        print(">> 操作：驳回")
        context._change_state(ProjectStatesEnum.APPROVED.value)

    @staticmethod
    def approve(context, **kwarg):
        print(">> 操作：通过移交申请")
        context._change_state(ProjectStatesEnum.FINISHED.value)


class ProjectFinishedState(ProjectState):
    """状态：已结束"""
    @property
    def value(self):
        return ProjectStatesEnum.FINISHED.value


# -------------------------------------
# 新增状态
# -------------------------------------
# class ProjectTerminationApplyingState(ProjectState):
#     """状态：终止申请中"""
#     @property
#     def value(self):
#         return ProjectStatesEnum.TERMINATION_APPLYING.value

#     @staticmethod
#     def drawback(context, **kwarg):
#         print(">> 操作：撤回")
#         context._change_state(ProjectStatesEnum.APPROVED.value)

#     @staticmethod
#     def refuse(context, **kwarg):
#         print(">> 操作：驳回")
#         context._change_state(ProjectStatesEnum.APPROVED.value)

#     @staticmethod
#     def approve(context, **kwarg):
#         print(">> 操作：通过终止申请")
#         context._change_state(ProjectStatesEnum.TERMINATED.value)


# class ProjectTerminatedState(ProjectState):
#     """状态：已终止"""
#     @property
#     def value(self):
#         return ProjectStatesEnum.TERMINATED.value


if __name__ == '__main__':

    print("新建项目")
    project = ProjectContext(ProjectStatesEnum.SAVED.value)
    print("当前状态：", project.state.value)
    os.system("pause")

    # 编辑
    project.handle('update')
    print("当前状态：", project.state.value)
    os.system("pause")

    # 提交
    project.handle('submit')
    print("当前状态：", project.state.value)
    os.system("pause")

    # 驳回
    project.handle('refuse')
    print("当前状态：", project.state.value)
    os.system("pause")

    # 再次提交
    project.handle('submit')
    print("当前状态：", project.state.value)
    os.system("pause")

    # 通过
    project.handle('approve')
    print("当前状态：", project.state.value)
    os.system("pause")

    # 已审批状态下不可编辑
    try:
        project.handle('update')
    except NotSupportOperation as e:
        print(e)
    print("当前状态：", project.state.value)
    os.system("pause")

    # # 申请终止
    # project.handle('terminate')
    # print("当前状态：", project.state.value)
    # os.system("pause")

    # # 通过
    # project.handle('approve')
    # print("当前状态：", project.state.value)
    # os.system("pause")
