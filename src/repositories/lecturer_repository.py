from src.models import Course, Lecturer


class LecturerRepository:
    def __init__(self, lecturer: Lecturer):
        """Connect to DB."""
        self.lecturer = lecturer


    def create(self):
        """Create new lecturer in DB."""

    def read(self):
        """Read lecturer in DB."""

    def delete(self):
        """Delete lecturer in DB."""

    def update(self):
        """Update lecturer in DB."""

    def exists(self):
        """Check if lecturer exists in DB."""

    def assign_a_course(self, course: Course):
        """Assign a course to lecturer."""