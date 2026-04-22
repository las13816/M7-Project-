from dataclasses import dataclass

@dataclass
class ScheduleItem:
    subject: str
    catalog: str
    section: str
    component: str
    session: str
    units: int
    tot_enrl: int
    cap_enrl: int
    instructor: str

    def get_key(self):
        """Return unique dictionary key"""
        return f"{self.subject}_{self.catalog}_{self.section}"

    def print(self):
        """Print formatted row"""
        print(f"{self.subject:<6} {self.catalog:<7} {self.section:<7} "
              f"{self.component:<9} {self.session:<6} {self.units:<5} "
              f"{self.tot_enrl:<7} {self.cap_enrl:<7} {self.instructor}")