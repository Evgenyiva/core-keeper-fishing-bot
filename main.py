from activities.MainActivity import MainActivity
from activities.View import View


def runApplication():
    # Init View
    view = View()
    # Init Activity
    activity = MainActivity(view)
    # bind view to activity
    view.setActivity(activity)

    # show Window in constant Loop
    view.show()

    # close window before exit application
    view.root.close()
    exit(0)


if __name__ == '__main__':
    runApplication()
